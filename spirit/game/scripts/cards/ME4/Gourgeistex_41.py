from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="79f0dadb-a447-51f4-93cc-2b18d2348a46",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gourgeistex.Name",
    display_name="Gourgeist ex",
    searchable_by=["Gourgeist ex", "Stage 1", "ex", "Gourgeistex"],
    subtypes=["Stage 1", "ex"],
    collector_number=41,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    family_id=710,
    abilities=[
        Attack(
            title="Horrifying Rondo",
            game_text="This attack does 50 more damage for each of your Benched Pokémon that has any damage counters on it.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Ghostly Touch",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
