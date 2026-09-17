from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c4bd9366-b4d4-5a31-b53f-287bac195dfd',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name',
    display_name='Delphox',
    searchable_by=['Delphox', 'Stage 2', 'Delphox'],
    subtypes=['Stage 2'],
    collector_number=26,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name',
    family_id=653,
    abilities=[
        Ability(
            title='Mystical Fire',
            game_text='Once during your turn (before your attack), you may draw cards until you have 6 cards in your hand.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Blaze Ball',
            game_text='This attack does 20 more damage for each Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
