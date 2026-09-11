from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7b83b477-5681-5704-b03f-b6dd4137a3d3',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sunflora.Name',
    display_name='Sunflora',
    searchable_by=['Sunflora', 'Stage 1', 'Sunflora'],
    subtypes=['Stage 1'],
    collector_number=8,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name',
    family_id=191,
    abilities=[
        Attack(
            title='Solar Power',
            game_text='During your next turn, ignore all Energy in the attack costs of Grass Pokémon and Fire Pokémon. (This includes Pokémon that come into play on that turn.)',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Solar Beam',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
