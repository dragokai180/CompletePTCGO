from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
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
    guid="dbfd0485-77f9-50e6-9a6c-067c847ef92c",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    display_name="Spinarak",
    searchable_by=["Spinarak","Basic","Spinarak"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    family_id=167,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
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
