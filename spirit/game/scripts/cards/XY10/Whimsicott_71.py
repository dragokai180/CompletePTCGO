from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='61903476-df42-5d45-b810-fb71a133e052',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name',
    display_name='Whimsicott',
    searchable_by=['Whimsicott', 'Stage 1', 'Whimsicott'],
    subtypes=['Stage 1'],
    collector_number=71,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name',
    family_id=546,
    abilities=[
        Attack(
            title='Light Steps',
            game_text='Move an Energy from this Pokémon to 1 of your Benched Pokémon.',
            cost={PokemonTypes.FAIRY: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
