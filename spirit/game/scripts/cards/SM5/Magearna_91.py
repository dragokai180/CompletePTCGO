from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='324844c4-059e-5c54-9f8e-d1ea1336dbad',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magearna.Name',
    display_name='Magearna',
    searchable_by=['Magearna', 'Basic', 'Magearna'],
    subtypes=['Basic'],
    collector_number=91,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=801,
    abilities=[
        Ability(
            title='Change Clothes',
            game_text='Once during your turn (before your attack), you may put a Pokémon Tool card attached to 1 of your Pokémon into your hand.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Rolling Attack',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
