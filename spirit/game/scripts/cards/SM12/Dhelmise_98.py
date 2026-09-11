from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1c7c0d32-0a52-5669-909f-772c1cb84a48',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name',
    display_name='Dhelmise',
    searchable_by=['Dhelmise', 'Basic', 'Dhelmise'],
    subtypes=['Basic'],
    collector_number=98,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=781,
    abilities=[
        Attack(
            title='Seaweed Grab',
            game_text='Put a Trainer card from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Buster Swing',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
