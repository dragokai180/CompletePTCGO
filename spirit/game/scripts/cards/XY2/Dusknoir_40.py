from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0d98eb2a-073f-59e0-85ce-e14f5a1842d7',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name',
    display_name='Dusknoir',
    searchable_by=['Dusknoir', 'Stage 2', 'Dusknoir'],
    subtypes=['Stage 2'],
    collector_number=40,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name',
    family_id=355,
    abilities=[
        Ability(
            title='Shadow Void',
            game_text='As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Pokémon to this Pokémon.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Pain Pellets',
            game_text="Put damage counters on 1 of your opponent's Pokémon equal to the number of damage counters on this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
