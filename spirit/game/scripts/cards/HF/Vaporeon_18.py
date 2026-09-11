from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f2f7697a-e424-5ad4-9992-5b4a6ad88ce7',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name',
    display_name='Vaporeon',
    searchable_by=['Vaporeon', 'Stage 1', 'Vaporeon'],
    subtypes=['Stage 1'],
    collector_number=18,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Bubble Drain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
