from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d171c461-9fd7-52ec-99ff-acd4c7f8841a',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name',
    display_name='Zebstrika',
    searchable_by=['Zebstrika', 'Stage 1', 'Zebstrika'],
    subtypes=['Stage 1'],
    collector_number=63,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name',
    family_id=522,
    abilities=[
        Attack(
            title='Burst of Braying',
            game_text='Choose Basic Lightning Energy cards from your discard pile up to the number of Prize cards your opponent has taken and attach them to your Pokémon in any way you like.',
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Thunder',
            game_text='This Pokémon also does 50 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
