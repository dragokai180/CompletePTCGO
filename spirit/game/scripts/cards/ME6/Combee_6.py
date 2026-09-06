from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import remove_self_from_play
from spirit.game.session.effects import is_pokemon_card


def _has_bug_out(card):
    definition = def_for(getattr(card, "archetype_id", None) or "")
    for ability in getattr(definition, "abilities", None) or []:
        if getattr(ability, "title", None) == "Bug Out":
            return True
    return False


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
    guid="3c17f6f1-d804-5295-9c82-ec9532b660a3",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    display_name="Combee",
    searchable_by=["Combee","Basic","Combee"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    family_id=415,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Attack(
            title="Fade Out",
            game_text="Put this Pokémon and all attached cards into your hand.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=remove_self_from_play("hand"),
        ),
        Attack(
            title="Bug Out",
            game_text="Reveal the bottom 7 cards of your deck, and this attack does 50 damage for each Pokémon you find there that has the Bug Out attack. Then, shuffle any revealed Pokémon back into your deck. Discard the other cards.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=bug_out,
        ),
    ],
)
