from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9eb1697f-42bb-58a6-9a40-68fe2daa79ff',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name',
    display_name='Gothitelle',
    searchable_by=['Gothitelle', 'Stage 2', 'Gothitelle'],
    subtypes=['Stage 2'],
    collector_number=41,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name',
    family_id=574,
    abilities=[
        Ability(
            title='Teleport Room',
            game_text='Once during your turn (before your attack), you may discard any Stadium card in play. If you do, put a Stadium card with a different name from your discard pile into play.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Psy Report',
            game_text='Your opponent reveals his or her hand.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
