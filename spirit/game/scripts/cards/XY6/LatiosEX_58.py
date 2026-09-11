from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d0cde4e-e7fa-5d95-bf1e-29e6c18ed9a7',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LatiosEX.Name',
    display_name='Latios-EX',
    searchable_by=['Latios-EX', 'Basic', 'EX', 'LatiosEX'],
    subtypes=['Basic', 'EX'],
    collector_number=58,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=381,
    abilities=[
        Attack(
            title='Fast Raid',
            game_text='If you go first, you can use this attack on your first turn.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Light Pulse',
            game_text="Prevent all effects of your opponent's attacks, except damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
