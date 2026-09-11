from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='efcf3d74-4c16-5430-8be9-b5bd24a30fcc',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name',
    display_name='Seismitoad',
    searchable_by=['Seismitoad', 'Stage 2', 'Seismitoad'],
    subtypes=['Stage 2'],
    collector_number=117,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name',
    family_id=535,
    abilities=[
        Ability(
            title='Bulldoze',
            game_text='Once during your turn (before your attack), you may search your deck for a card, shuffle your deck, then put that card on top of it.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Tremulous Fist',
            game_text='This attack does 30 more damage for each of your Benched Pokémon that has any damage counters on it.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
