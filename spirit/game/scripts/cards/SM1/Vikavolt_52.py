from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='94b9d9b7-5ccf-5cf9-bf94-4df54aa59e5d',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name',
    display_name='Vikavolt',
    searchable_by=['Vikavolt', 'Stage 2', 'Vikavolt'],
    subtypes=['Stage 2'],
    collector_number=52,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name',
    family_id=736,
    abilities=[
        Ability(
            title='Strong Charge',
            game_text='Once during your turn (before your attack), you may search your deck for a Grass Energy card and a Lightning Energy card and attach them to your Pokémon in any way you like. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Electro Cannon',
            game_text='Discard 3 Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
