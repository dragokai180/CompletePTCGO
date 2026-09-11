from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a297ee97-6413-5dc3-9f90-90c0ecac26b5',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name',
    display_name='Camerupt',
    searchable_by=['Camerupt', 'Stage 1', 'Camerupt'],
    subtypes=['Stage 1'],
    collector_number=12,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name',
    family_id=322,
    abilities=[
        Attack(
            title='Super Singe',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Cinder Cannon',
            game_text='You may discard a Fighting Energy from this Pokémon. If you do, this attack does 120 more damage.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
