from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0af78f68-3867-5101-abce-eba0426f37ab',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SylveonEX.Name',
    display_name='Sylveon-EX',
    searchable_by=['Sylveon-EX', 'Basic', 'EX', 'SylveonEX'],
    subtypes=['Basic', 'EX'],
    collector_number=121,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=700,
    abilities=[
        Attack(
            title='Dress Up',
            game_text='If this Pokémon has a Pokémon Tool card attached to it, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Precious Ribbon',
            game_text='Move a Fairy Energy from this Pokémon to 1 of your Benched Pokémon. If you do, heal 50 damage from that Pokémon.',
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
