from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ae0d38ab-1605-535f-9c24-ffbe33d5d43a',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShayminEX.Name',
    display_name='Shaymin-EX',
    searchable_by=['Shaymin-EX', 'Basic', 'EX', 'ShayminEX'],
    subtypes=['Basic', 'EX'],
    collector_number=77,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=492,
    abilities=[
        Ability(
            title='Set Up',
            game_text='When you play this Pokémon from your hand onto your Bench, you may draw cards until you have 6 cards in your hand.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Sky Return',
            game_text='Return this Pokémon and all cards attached to it to your hand.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
