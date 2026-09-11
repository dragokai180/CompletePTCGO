from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b9275f7e-1c43-5bc4-8250-a3b373d21b49',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonEX.Name',
    display_name='Leafeon-EX',
    searchable_by=['Leafeon-EX', 'Basic', 'EX', 'LeafeonEX'],
    subtypes=['Basic', 'EX'],
    collector_number=10,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=470,
    abilities=[
        Attack(
            title='Leaf Blade',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title="Nature's Breath",
            game_text='If there is any Stadium card in play, this attack does 30 more damage and heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
