from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks
from spirit.game.session.effects import is_pokemon_card


def _has_bug_out(card):
    definition = def_for(getattr(card, "archetype_id", None) or "")
    for ability in getattr(definition, "abilities", None) or []:
        if getattr(ability, "title", None) == "Bug Out":
            return True
    return False


async def scary_pattern(ctx):
    """30. During your opponent's next turn, the Defending Pokémon can't attack."""
    await ctx.deal_damage()
    lock_defender_attacks(ctx)


async def bug_out(ctx):
    """Reveal the bottom 7 cards; 50 damage per Pokémon with Bug Out.
    Shuffle revealed Pokémon back; discard the rest."""
    bottom = ctx.deck()[:7]
    if bottom:
        await ctx.reveal_cards(bottom)
    hits = sum(1 for c in bottom if is_pokemon_card(c) and _has_bug_out(c))
    others = [c for c in bottom if not is_pokemon_card(c)]
    if others:
        await ctx.discard_cards(others)
    await ctx.shuffle_deck()
    if hits:
        await ctx.deal_damage(50 * hits)


card = PokemonCardDef(
    guid="89c41df5-d11e-5fa4-a82e-e11b737ae74b",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain","Stage 1","Masquerain"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    family_id=283,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    abilities=[
        Attack(
            title="Scary Pattern",
            game_text="During your opponent's next turn, the Defending Pokémon can't use attacks.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=scary_pattern,
        ),
        Attack(
            title="Bug Out",
            game_text="Reveal the bottom 7 cards of your deck, and this attack does 50 damage for each Pokémon you find there that has the Bug Out attack. Then, shuffle any revealed Pokémon back into your deck. Discard the other cards.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            damage_operator="x",
            effect=bug_out,
        ),
    ],
)
