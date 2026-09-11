from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='919ae753-fcb6-5965-b628-3221c3def5b8',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name',
    display_name='Golurk',
    searchable_by=['Golurk', 'Stage 1', 'Golurk'],
    subtypes=['Stage 1'],
    collector_number=35,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name',
    family_id=622,
    abilities=[
        Ability(
            title='Double Type',
            game_text='As long as this Pokémon is in play, it is Psychic and Fighting type.',
            passive=standard_passive('As long as this Pokémon is in play, it is Psychic and Fighting type.'),
        ),
        Attack(
            title='Superpower',
            game_text='You may do 40 more damage. If you do, this Pokémon does 20 damage to itself.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon."),
)
