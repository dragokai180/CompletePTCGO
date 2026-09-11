from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='02a7a734-e49e-59dd-aa19-5d223db6312a',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name',
    display_name='Flaaffy',
    searchable_by=['Flaaffy', 'Stage 1', 'Flaaffy'],
    subtypes=['Stage 1'],
    collector_number=15,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name',
    family_id=179,
    abilities=[
        Attack(
            title='Static Shock',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title='Extreme Current',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
