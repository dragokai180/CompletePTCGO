from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7f5755d8-1d88-547b-b047-b0bf0f9c8e6a',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name',
    display_name='Frogadier',
    searchable_by=['Frogadier', 'Stage 1', 'Frogadier'],
    subtypes=['Stage 1'],
    collector_number=57,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name',
    family_id=656,
    abilities=[
        Attack(
            title='Strafe',
            game_text='You may switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
