from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
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
    guid="0c1dc4c8-1b57-5eca-bd03-32a2a2e04d8a",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    display_name="Sizzlipede",
    searchable_by=["Sizzlipede","Basic","Sizzlipede"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=850,
    abilities=[
        Attack(
            title="Controlled Burn",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=mill_attack(1),
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
