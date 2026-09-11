from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9e175600-e3b0-56f0-9d3b-74a12c0d0382',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arboliva.Name',
    display_name='Arboliva',
    searchable_by=['Arboliva', 'Stage 2', 'Arboliva'],
    subtypes=['Stage 2'],
    collector_number=21,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name',
    family_id=928,
    abilities=[
        Attack(
            title='Healing Fruit',
            game_text='Heal all damage from 1 of your Benched Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Oil Shot',
            cost={PokemonTypes.GRASS: 1},
            damage=90,
        ),
    ],
)
