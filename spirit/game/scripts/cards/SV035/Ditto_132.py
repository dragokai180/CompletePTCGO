from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='52692a5e-31c2-5da1-b14b-b3f734510433',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name',
    display_name='Ditto',
    searchable_by=['Ditto', 'Basic', 'Ditto'],
    subtypes=['Basic'],
    collector_number=132,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=132,
    abilities=[
        Ability(
            title='Transformative Start',
            game_text='Once during your first turn, if this Pokémon is in the Active Spot, you may search your deck and choose a Basic Pokémon you find there, except any Ditto. If you do, discard this Pokémon and all attached cards, and put the chosen Pokémon in its place. Then, shuffle your deck.',
            passive=standard_passive('Once during your first turn, if this Pokémon is in the Active Spot, you may search your deck and choose a Basic Pokémon you find there, except any Ditto. If you do, discard this Pokémon and all attached cards, and put the chosen Pokémon in its place. Then, shuffle your deck.'),
        ),
        Attack(
            title='Splup',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
