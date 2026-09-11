from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f46d1d42-ff21-5633-84d5-0eaae89c57bb',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.FlareonEX.Name',
    display_name='Flareon-EX',
    searchable_by=['Flareon-EX', 'Basic', 'EX', 'FlareonEX'],
    subtypes=['Basic', 'EX'],
    collector_number=106,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=136,
    abilities=[
        Ability(
            title='Flash Fire',
            game_text='Once during your turn (before your attack), you may move a Fire Energy from 1 of your Pokémon to this Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Blaze Ball',
            game_text='This attack does 20 more damage for each Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
