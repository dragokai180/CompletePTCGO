from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5456f342-bf29-5669-9dbe-463ed235f594',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name',
    display_name='Dedenne',
    searchable_by=['Dedenne', 'Basic', 'Dedenne'],
    subtypes=['Basic'],
    collector_number=34,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Attack(
            title='Entrainment',
            game_text='Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Energy Short',
            game_text="This attack does 20 damage times the amount of Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
