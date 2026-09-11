from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='16e2599e-80ff-531f-b632-e87ee53491a6',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LunalaGX.Name',
    display_name='Lunala-GX',
    searchable_by=['Lunala-GX', 'Stage 2', 'GX', 'LunalaGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=66,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name',
    family_id=789,
    abilities=[
        Ability(
            title='Psychic Transfer',
            game_text='As often as you like during your turn (before your attack), you may move a Psychic Energy from 1 of your Pokémon to another of your Pokémon.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Moongeist Beam',
            game_text="The Defending Pokémon can't be healed during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 4},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Lunar Fall-GX',
            game_text="Knock Out 1 of your opponent's Basic Pokémon that isn't a Pokémon-GX. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
