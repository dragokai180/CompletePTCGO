from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4b961dc2-f6c7-5f8c-9a4b-b56b9333dfca',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.NinetalesEX.Name',
    display_name='Ninetales-EX',
    searchable_by=['Ninetales-EX', 'Basic', 'EX', 'NinetalesEX'],
    subtypes=['Basic', 'EX'],
    collector_number=13,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=38,
    abilities=[
        Attack(
            title='Flare Bonus',
            game_text='Discard a Fire Energy card from your hand. If you do, draw 3 cards.',
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fire Blast',
            game_text='Flip a coin. If tails, discard a Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
