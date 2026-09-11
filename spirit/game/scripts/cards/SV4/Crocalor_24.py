from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f47a07a1-cafc-502b-a09e-3b3c36d1ca34',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name',
    display_name='Crocalor',
    searchable_by=['Crocalor', 'Stage 1', 'Crocalor'],
    subtypes=['Stage 1'],
    collector_number=24,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name',
    family_id=909,
    abilities=[
        Attack(
            title='Rolling Fireball',
            game_text='Put an Energy attached to this Pokémon into your hand.',
            cost={PokemonTypes.FIRE: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
