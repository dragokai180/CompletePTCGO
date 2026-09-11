from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b63ff14d-7d72-5bc4-8670-21021ab84e3f',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Klawf.Name',
    display_name='Klawf',
    searchable_by=['Klawf', 'Basic', 'Klawf'],
    subtypes=['Basic'],
    collector_number=122,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=950,
    abilities=[
        Attack(
            title='Vise Grip',
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
        Attack(
            title='Adrenaline Hammer',
            game_text='This Pokémon is now Confused.',
            cost={PokemonTypes.FIGHTING: 3},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
