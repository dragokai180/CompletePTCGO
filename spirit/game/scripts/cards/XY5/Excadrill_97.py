from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='02194f91-1cf9-5545-a071-4eb0f51d99ca',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Excadrill.Name',
    display_name='Excadrill',
    searchable_by=['Excadrill', 'Stage 1', 'Excadrill'],
    subtypes=['Stage 1'],
    collector_number=97,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name',
    family_id=529,
    abilities=[
        Attack(
            title='Dredge',
            game_text='Search your deck for 2 Energy cards and attach them to this Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mach Claw',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("This Pokémon may attack twice a turn. (If the first attack Knocks Out your opponent's Active Pokémon, you may attack again after your opponent chooses a new Active Pokémon.)"),
)
