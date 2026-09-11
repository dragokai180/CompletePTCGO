from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0509c328-99c1-5f2d-acc7-d075d623c6e9',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name',
    display_name='Pupitar',
    searchable_by=['Pupitar', 'Stage 1', 'Pupitar'],
    subtypes=['Stage 1'],
    collector_number=106,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name',
    family_id=246,
    abilities=[
        Attack(
            title='Rock Throw',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title='Blasting Tackle',
            game_text="This attack also does 20 damage to 1 of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
