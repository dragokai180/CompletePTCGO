from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4f0822c3-4a53-58c2-aaaa-64126e88021b',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name',
    display_name='Ludicolo',
    searchable_by=['Ludicolo', 'Stage 2', 'Ludicolo'],
    subtypes=['Stage 2'],
    collector_number=38,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name',
    family_id=270,
    abilities=[
        Ability(
            title='Swing Dance',
            game_text='Once during your turn (before your attack), you may draw a card.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Circular Steps',
            game_text="This attack does 10 more damage for each other Pokémon in play (both yours and your opponent's).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
