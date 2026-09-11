from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='78f6eef0-1817-562c-8bb3-03eb508e1757',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name',
    display_name='Hakamo-o',
    searchable_by=['Hakamo-o', 'Stage 1', 'Hakamoo'],
    subtypes=['Stage 1'],
    collector_number=162,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name',
    family_id=782,
    abilities=[
        Ability(
            title="Fighter's Roar",
            game_text="If your opponent's Active Pokémon is a Pokémon-GX or Pokémon-EX, this Pokémon can evolve during the turn you play it.",
            passive=standard_passive("If your opponent's Active Pokémon is a Pokémon-GX or Pokémon-EX, this Pokémon can evolve during the turn you play it."),
        ),
        Attack(
            title='Dragonslice',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
    ],
)
