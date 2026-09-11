from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ba81e28a-ce77-5e8a-90ba-60b52eae308f',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name',
    display_name='Slaking',
    searchable_by=['Slaking', 'Stage 2', 'Slaking'],
    subtypes=['Stage 2'],
    collector_number=115,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name',
    family_id=287,
    abilities=[
        Ability(
            title='Lazy',
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Pokémon in play have no Abilities, except for Lazy.",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, your opponent's Pokémon in play have no Abilities, except for Lazy."),
        ),
        Attack(
            title='Critical Move',
            game_text="Discard an Energy from this Pokémon. It can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
