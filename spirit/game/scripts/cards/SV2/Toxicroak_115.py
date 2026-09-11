from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7e207f70-95d8-561f-849d-d86f9fc91739',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name',
    display_name='Toxicroak',
    searchable_by=['Toxicroak', 'Stage 1', 'Toxicroak'],
    subtypes=['Stage 1'],
    collector_number=115,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name',
    family_id=453,
    abilities=[
        Attack(
            title='Pierce',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title='Knuckle Claws',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
