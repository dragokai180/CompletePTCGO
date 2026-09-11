from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2952964d-7666-591e-bf4a-0a3a34687020',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name',
    display_name='Kakuna',
    searchable_by=['Kakuna', 'Stage 1', 'Kakuna'],
    subtypes=['Stage 1'],
    collector_number=4,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name',
    family_id=13,
    abilities=[
        Ability(
            title='Grass Cushion',
            game_text='If this Pokémon has any Grass Energy attached to it, it takes 30 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('If this Pokémon has any Grass Energy attached to it, it takes 30 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
