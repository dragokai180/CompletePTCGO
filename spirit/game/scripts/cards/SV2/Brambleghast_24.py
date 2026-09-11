from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e2829ce2-fe50-56b7-8291-3de879c86367',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Brambleghast.Name',
    display_name='Brambleghast',
    searchable_by=['Brambleghast', 'Stage 1', 'Brambleghast'],
    subtypes=['Stage 1'],
    collector_number=24,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name',
    family_id=946,
    abilities=[
        Attack(
            title='Absorb Life',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Dead Wood Detention',
            game_text="During your opponent's next turn, attacks that the Defending Pokémon uses cost ColorlessColorless more.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
