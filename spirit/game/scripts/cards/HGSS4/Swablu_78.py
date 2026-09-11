from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='37941b24-8426-5d70-9154-87e9dbb93cc8',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name',
    display_name='Swablu',
    searchable_by=['Swablu', 'Basic', 'Swablu'],
    subtypes=['Basic'],
    collector_number=78,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=333,
    abilities=[
        Attack(
            title='Wing Flick',
            game_text='Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
