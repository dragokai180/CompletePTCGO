from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e99c4014-b252-55c3-807f-98d71c354c2d',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name',
    display_name='Goodra',
    searchable_by=['Goodra', 'Stage 2', 'Goodra'],
    subtypes=['Stage 2'],
    collector_number=74,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name',
    family_id=704,
    abilities=[
        Ability(
            title='Gooey Regeneration',
            game_text='As often as you like during your turn (before your attack), you may discard an Energy attached to this Pokémon. If you do, heal 60 damage from this Pokémon.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Heavy Whip',
            game_text='Flip a coin. If heads, this attack does 40 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
