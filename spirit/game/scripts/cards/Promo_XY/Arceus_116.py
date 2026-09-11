from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b709642c-3498-53d3-9804-bbf2c7537c23',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name',
    display_name='Arceus',
    searchable_by=['Arceus', 'Basic', 'Arceus'],
    subtypes=['Basic'],
    collector_number=116,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=493,
    abilities=[
        Attack(
            title='Type Switch',
            game_text='Choose Grass, Fire, Water, Lightning, Psychic, Fighting, Darkness, Metal, Fairy, or Dragon type. Until the ends of your next turn, this Pokémon is that type.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Power Blast',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
