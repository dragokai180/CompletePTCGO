from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d35f2206-3851-5262-8d6c-d1a0c71ae4de',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grafaiai.Name',
    display_name='Grafaiai',
    searchable_by=['Grafaiai', 'Stage 1', 'Grafaiai'],
    subtypes=['Stage 1'],
    collector_number=146,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name',
    family_id=944,
    abilities=[
        Attack(
            title='Spit Poison',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Colorful Graffiti',
            game_text='You may discard as many Basic Energy cards as you like from your hand. This attack does 40 damage for each type of Basic Energy you discarded in this way.',
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
