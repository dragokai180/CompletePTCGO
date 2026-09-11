from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="6cf39700-962c-509b-b86c-b88c28792d20",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spectrier.Name",
    display_name="Spectrier",
    searchable_by=["Spectrier", "Basic", "Spectrier"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=897,
    abilities=[
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Phantasmal Barrage",
            game_text="Discard all Energy from this Pokémon and place 12 damage counters on 1 of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
