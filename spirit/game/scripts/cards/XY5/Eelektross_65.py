from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6d39d43a-79ab-5b26-bdbb-7fca309e8ec8',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eelektross.Name',
    display_name='Eelektross',
    searchable_by=['Eelektross', 'Stage 2', 'Eelektross'],
    subtypes=['Stage 2'],
    collector_number=65,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name',
    family_id=602,
    abilities=[
        Ability(
            title='Energy Connect',
            game_text='As often as you like during your turn (before your attack), you may move a basic Energy attached to 1 of your Benched Pokémon to your Active Pokémon.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Electricannon',
            game_text='You may discard all Lightning Energy attached to this Pokémon. If you do, this attack does 50 more damage.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
