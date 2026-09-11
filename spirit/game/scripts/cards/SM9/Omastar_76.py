from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ce08bdcc-1f1e-5c74-8b16-147aa1636218',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name',
    display_name='Omastar',
    searchable_by=['Omastar', 'Stage 2', 'Omastar'],
    subtypes=['Stage 2'],
    collector_number=76,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name',
    family_id=138,
    abilities=[
        Ability(
            title='Fossil Bind',
            game_text="As long as you have fewer Pokémon in play than your opponent, they can't play any Item cards from their hand.",
            passive=standard_passive("As long as you have fewer Pokémon in play than your opponent, they can't play any Item cards from their hand."),
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
