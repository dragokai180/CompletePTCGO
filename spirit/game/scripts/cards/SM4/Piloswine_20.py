from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb1de76e-c82a-5232-8e35-a3c6a8b2d19c',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name',
    display_name='Piloswine',
    searchable_by=['Piloswine', 'Stage 1', 'Piloswine'],
    subtypes=['Stage 1'],
    collector_number=20,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name',
    family_id=220,
    abilities=[
        Attack(
            title='Stampede',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title='Rest',
            game_text='This Pokémon is now Asleep. Heal 90 damage from it.',
            cost={PokemonTypes.COLORLESS: 4},
            effect=standard_attack,
        ),
    ],
)
