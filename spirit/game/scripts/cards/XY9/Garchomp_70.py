from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='40e40b77-e00b-521a-ad31-9875c2ea2b7b',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name',
    display_name='Garchomp',
    searchable_by=['Garchomp', 'Stage 2', 'Garchomp'],
    subtypes=['Stage 2'],
    collector_number=70,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name',
    family_id=443,
    abilities=[
        Attack(
            title='Turbo Assault',
            game_text='Attach an Energy card from your discard pile to 1 of your Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Bite Off',
            game_text="If your opponent's Active Pokémon is a Pokémon-EX, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
